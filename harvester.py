
class harvester:
    """
    This class helps us keep track of our harvest. Its purpose is twofold:

    - Calculate the total weight of a certain crop type relative to the entire harvest.
    - Compute the rank of a certain crop type based on its ratio.

    There are some bugs in this class. Please fix them so that the methods work as intended.
    """

    def __init__(self):
        self.total_weight = 0
        self.crops = []

    def add(self, crop, weight):
        """
        This function allows to add new crops. The same crop type might be added multiple times,
        increasing the relative weight of the respective crop.

        :param crop: The name of the crop type.
        :param weight: The weight of the crop.
        :return: None
        """
        self.crops.append(crop)
        self.total_weight = self.total_weight + weight

    def get_ratio(self, crop):
        """
        The weight ratio of the provided crop relative to the weight of all crops.

        :param crop: The name of the crop type for which to calculate the relative weight.
        :return: The weight ratio of the provided crop relative to the weight of all crops.
        """
        return self.total_weight

    def get_ranked_crop(self, rank):
        """
        This function returns the crop type for the specified rank. The higher the total weight of a crop type lower the rank.
        Ranks start at 0.

        :param rank: The rank of the crop to look for.
        :return: The crop type for the specified rank.
        """
        return None