"""
.. module:: models
   :noindex:

.. header:: Data models and handling functions for exports/imports

.. moduleauthor:: Alex Glock
"""
import json
import os
from settings import BASE_DIR
from json import JSONEncoder


class Obj:
    """Custom class for Obj JSON handling."""

    def __init__(
        self,
        att1,
        att2,
        att3,
        list
    ):
        self.att1 = att1
        self.att1 = att2
        self.att1 = att3
        self.list = list


class NestedObj:
    """Custom class for NestedObj JSON handling."""

    def __init__(
        self,
        att1,
        att2,
        att3
    ):
        self.att1 = att1
        self.att1 = att2
        self.att1 = att3


def json_encoder(obj):
    """This function encodes a Python class back to the JSON format.

    :param obj: a board instance
    :type obj: BOARD as defined above
    :return: json parsed config file
    :rtype: JSON
    """
    obj_dictionary = obj.__dict__
    type_dictionary = {"__type__": type(obj).__name__}
    return {**type_dictionary, **obj_dictionary}


def json_decoder(jsonDict):
    """This function decodes a JSON file to python objects.

    :param jsonDict: content of the JSON file
    :type jsonDict: json dictionary
    :return: one Obj containing multiple NestedObj
    :rtype: Obj and NestedObj's
    """
    if "__type__" in jsonDict and jsonDict["__type__"] == "Obj":
        return Obj(
            jsonDict["att1"],
            jsonDict["att2"],
            jsonDict["att3"],
            jsonDict["list"]
        )
    if "__type__" in jsonDict and jsonDict["__type__"] == "NestedObj":
        return NestedObj(
            jsonDict["att1"],
            jsonDict["att2"],
            jsonDict["att3"]
        )


def load_nested_object():
    """This functions loads the Objects from the json file(s).

    :return: nested list of Objects as defined in the JSON.
    :rtype: Obj and NestedObj
    """
    nested_object_list = []
    json_dir = os.path.join(BASE_DIR, "json_handling")

    # get all json filenames
    json_filenames = [
        filename
        for filename in os.listdir(json_dir)
        if filename.endswith(".json")
    ]

    for json_file_name in json_filenames:
        filepath = os.path.join(json_dir, json_file_name)
        try:
            json_file = open(filepath)
            nested_object_list.append(
                json.load(json_file, object_hook=json_decoder)
            )
            json_file.close()
        except Exception as ex:
            print("Exception occured: %s", str(ex))
            pass

    return nested_object_list


def save_nested_object(obj, filepath):
    """This function saves changes in a Obj back to the JSON file

    :param Obj: a instance of Obj containing NestedObj
    :type: Obj class
    :param filepath: abs. system path to JSON
    :type: string
    """

    # encode altered Obj to json, override existing file
    if os.path.exists(filepath):
        with open(filepath, "w") as json_file:
            json.dump(obj, json_file, indent=4, default=json_encoder)
            json_file.close()
        return 0
    
    return 1
