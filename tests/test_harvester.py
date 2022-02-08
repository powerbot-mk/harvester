from harvester import harvester


def test_crop_ratio():
    cr = harvester()
    cr.add("wheat", 10)
    cr.add("potatoes", 15)
    cr.add("wheat", 7)
    cr.add("tomatoes", 2)

    wheat_ratio = cr.get_ratio("wheat")

    assert wheat_ratio == 0.5

    ranked_crop = cr.get_ranked_crop(2)

    assert ranked_crop == "tomatoes"


