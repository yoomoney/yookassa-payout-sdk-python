import re

from lxml import etree


class XMLHelper:
    @staticmethod
    def object_to_xml(obj):
        serializer = Object2XML()
        return serializer.parse(obj)

    @staticmethod
    def xml_to_object(xml):
        deserializer = XML2Object()
        return deserializer.parse(xml)


"""
Object2XML - Python Object to XML serialization

This code transforms a Python data structures into an XML document

Usage:
    serializer = Object2XML()
    xml_string = serializer.parse( python_object )
    print python_object
    print xml_string
"""


class Object2XML:

    def __init__(self):
        self.data = ""  # where we store the processed XML string

    def parse(self, obj, obj_name=None):
        """
        processes Python data structure into XML string
        needs objName if pythonObj is a List
        """
        if obj is None:
            return ""

        if isinstance(obj, dict):
            self.data = self._dict_to_xml(obj)

        elif isinstance(obj, list):
            # we need name for List object
            self.data = self._list_to_xml(obj, obj_name)

        else:
            self.data = "<%(n)s>%(o)s</%(n)s>" % {'n': obj_name, 'o': str(obj)}

        return self.data

    def _dict_to_xml(self, dict_obj, obj_name=None):
        """
        process Python Dict objects
        They can store XML attributes and/or children
        """
        tag_str = ""  # XML string for this level
        attributes = {}  # attribute key/value pairs
        attr_str = ""  # attribute string of this level
        child_str = ""  # XML string of this level's children

        for k, v in sorted(dict_obj.items(), key=lambda kv: kv[0], reverse=False):
            if isinstance(v, dict):
                # child tags, with attributes
                child_str += self._dict_to_xml(v, k)
            elif isinstance(v, list):
                # child tags, list of children
                child_str += self._list_to_xml(v, k)
            else:
                # tag could have many attributes, let's save until later
                attributes.update({k: v})

        if obj_name is None:
            return child_str

        # create XML string for attributes
        for k, v in sorted(attributes.items(), key=lambda kv: kv[0], reverse=False):
            attr_str += " %s=\"%s\"" % (k, v)

        # let's assemble our tag string
        if child_str == "":
            tag_str += "<%(n)s%(a)s />" % {'n': obj_name, 'a': attr_str}
        else:
            tag_str += "<%(n)s%(a)s>%(c)s</%(n)s>" % {'n': obj_name, 'a': attr_str, 'c': child_str}

        return tag_str

    def _list_to_xml(self, list_obj, obj_name=None):
        """
        process Python List objects
        They have no attributes, just children
        Lists only hold Dicts or Strings
        """
        tag_str = ""  # XML string for this level
        child_str = ""  # XML string of children

        for child_obj in list_obj:

            if isinstance(child_obj, dict):
                # here's some Magic
                # we're assuming that List parent has a plural name of child:
                # eg, persons > person, so cut off last char
                # name-wise, only really works for one level, however
                # in practice, this is probably ok
                child_str += self._dict_to_xml(child_obj, obj_name[:-1])
            elif child_obj is None:
                pass
            else:
                for string in child_obj:
                    child_str += string

        if obj_name is None:
            return child_str

        tag_str += "<%(n)s>%(c)s</%(n)s>" % {'n': obj_name, 'c': child_str}

        return tag_str


"""
XML2Object - XML to Python Object de-serialization

This code transforms an XML document into a Python data structure

Usage:
    deserializer = XML2Object()
    python_object = deserializer.parse( xml_string )
    print xml_string
    print python_object
"""


class XML2Object:

    def __init__(self):
        self._parser = etree.XMLParser(remove_blank_text=True)
        self._root = None  # root of etree structure
        self.data = None  # where we store the processed Python structure

    def parse(self, xml):
        """
        processes XML string into Python data structure
        """
        xml = re.search(r"<(\w+).*(</\1>|/>)", xml, flags=re.DOTALL)
        if xml:
            root = xml.group()
            self._root = etree.fromstring(root, self._parser)
            self.data = self._parse_xml_root()
            return self.data
        else:
            raise ValueError('Input text not contains root tag')

    def to_string(self):
        """
        creates a string representation using our etree object
        """
        if self._root is not None:
            return etree.tostring(self._root)

    def _parse_xml_root(self):
        """
        starts processing, takes care of first level idiosyncrasies
        """
        child_dict = self._parse_xml_node(self._root)
        return {self._root.tag: child_dict["children"]}

    def _parse_xml_node(self, element):
        """
        rest of the processing
        """
        # process any tag attributes
        # if we have attributes then the child container is a Dict
        #   otherwise a List
        if element.items():
            child_container = {}
            child_container.update(dict(element.items()))
        else:
            child_container = []

        if isinstance(child_container, list) and element.text:
            # tag with no attributes and one that contains text
            child_container.append(element.text)

        else:
            # tag might have children, let's process them
            for child_elem in element.getchildren():

                child_dict = self._parse_xml_node(child_elem)

                # let's store our child based on container type
                #
                if isinstance(child_container, dict):
                    # these children are lone tag entities ( eg, 'copyright' )
                    child_container.update({child_dict["tag"]: child_dict["children"]})

                else:
                    # these children are repeated tag entities ( eg, 'format' )
                    child_container.append(child_dict["children"])

        return {"tag": element.tag, "children": child_container}
