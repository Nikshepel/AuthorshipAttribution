import pickle
from ataurus.ml.model import Model


def serialize_model(model: Model, filename: str):
    """
    Serializes a model into the .pickle file.

    :param model: serializing model
    :param filename: the name of the file
    """
    if not isinstance(model, Model):
        raise ValueError("Serializing model isn't a Model instance")

    with open(filename, 'wb') as file:
        pickle.dump(model, file)


def deserialize_model(filename: str) -> Model:
    """
    Deserializes a model from a .pickle file.

    :param filename: the name of the file
    """
    with open(filename, 'rb') as file:
        return pickle.load(file)
