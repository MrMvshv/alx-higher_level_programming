#!/usr/bin/python3
""" first class Base
    with private class attribute __nb_objects
    public instance attribute id
"""
import json
import turtle
import csv


class Base:
    """ public instance attribute id
        private class attribute __nb_objects
        The goal of it is to manage id attribute
        in all your future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ base initializer
            init id to id if id != None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation
            of list_objs to a file
            list_objs is a list of instances who inherits of Base
        """
        nw_dicts = []
        filename = cls.__name__ + ".json"

        if list_objs is None or list_objs == []:
            nStr = "[]"
        else:
            for x in list_objs:
                y = x.to_dictionary()
                nw_dicts.append(y)
            nStr = list_objs[0].to_json_string(nw_dicts)

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(nStr)

    def from_json_string(json_string):
        """Return the deserialized JSON string.
           (str): A JSON str representation of a list of dicts.
           Return: If json_string is None or empty - an empty list.
           Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
           dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
            Return: If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def __del__(self):
        pass

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
            Opens a window and draws all the squares and rectangles
        '''
        import turtle as t

        t.title("Rectangles and Squares")
        t.penup()
        t.pensize(5)
        t.bgcolor("grey")
        t.color("green")
        t.hideturtle()
        t.goto(-275, 275)
        t.speed(2)

        for instance in list_rectangles:
            t.pendown()
            t.begin_fill()
            for i in range(2):
                t.forward(instance.width)
                t.right(90)
                t.forward(instance.height)
                t.right(90)
            t.end_fill()
            t.penup()
            move_by = instance.width + 25
            x_cordinate = round(t.xcor(), 5)
            t.goto(x_cordinate + move_by, 275)

        t.goto(-275, 0)
        for instance in list_squares:
            t.pendown()
            t.begin_fill()
            for i in range(2):
                t.forward(instance.width)
                t.right(90)
                t.forward(instance.height)
                t.right(90)
            t.end_fill()
            t.penup()
            move_by = instance.width + 25
            x_cordinate = round(t.xcor(), 5)
            t.goto(x_cordinate + move_by, 0)

        t.exitonclick()
