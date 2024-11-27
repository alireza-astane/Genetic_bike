from env.env import *
import unittest

assertions = unittest.TestCase("__init__")


def test_get_distance_unit_vector():
    test_env = env(9.8)
    R = np.array([[[1, 1], [2, 2], [3, 3], [4, 4]], [[1, 1], [2, 2], [3, 3], [4, 4]]])

    normalized_distances = test_env.get_distance_unit_vector(R)
    assert np.all(
        normalized_distances
        - np.array(
            [
                [
                    [
                        [0.0, 0.0],
                        [0.70710678, 0.70710678],
                        [0.70710678, 0.70710678],
                        [0.70710678, 0.70710678],
                    ],
                    [
                        [-0.70710678, -0.70710678],
                        [0.0, 0.0],
                        [0.70710678, 0.70710678],
                        [0.70710678, 0.70710678],
                    ],
                    [
                        [-0.70710678, -0.70710678],
                        [-0.70710678, -0.70710678],
                        [0.0, 0.0],
                        [0.70710678, 0.70710678],
                    ],
                    [
                        [-0.70710678, -0.70710678],
                        [-0.70710678, -0.70710678],
                        [-0.70710678, -0.70710678],
                        [0.0, 0.0],
                    ],
                ],
                [
                    [
                        [0.0, 0.0],
                        [0.70710678, 0.70710678],
                        [0.70710678, 0.70710678],
                        [0.70710678, 0.70710678],
                    ],
                    [
                        [-0.70710678, -0.70710678],
                        [0.0, 0.0],
                        [0.70710678, 0.70710678],
                        [0.70710678, 0.70710678],
                    ],
                    [
                        [-0.70710678, -0.70710678],
                        [-0.70710678, -0.70710678],
                        [0.0, 0.0],
                        [0.70710678, 0.70710678],
                    ],
                    [
                        [-0.70710678, -0.70710678],
                        [-0.70710678, -0.70710678],
                        [-0.70710678, -0.70710678],
                        [0.0, 0.0],
                    ],
                ],
            ]
        )
        < 1e-5
    )


def test_calculate_distance_from_ground():  ###? bikes ?
    test_env = env(9.8)
    pos = np.array([[1, 1], [2, 4], [3, 9]])
    distances, touch_index = test_env.calculate_distance_from_ground(pos)
    assert np.all(distances - np.array([0, np.sqrt(2), 3 * np.sqrt(2)]) < 1e-5)

    assert np.all(touch_index == np.array([1000, 3000, 6000]))


def test_evalute():
    test_env = env(9.8)
    test_env.R = np.array(
        [[[1, 1], [2, 2], [3, 3], [4, 4]], [[1, 1], [2, 2], [3, 3], [4, 4]]]
    )
    test_env.R0 = np.array(
        [[[1, 1], [2, 2], [3, 3], [4, 4]], [[1, 1], [2, 2], [3, 3], [4, 4]]]
    )
    assertions.assertAlmostEqual(test_env.evaluate(), np.zeros((2, 2)))


def test_get_K():
    my_env = env(9.8)

    my_bike_1 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_2 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_3 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_env.set_bikes([my_bike_1, my_bike_2, my_bike_3])

    assert np.all(
        my_env.get_K()
        == np.array(
            [
                [[1.0, 11.0], [4.0, 11.0], [1.0, 13.0], [4.0, 13.0]],
                [[1.0, 11.0], [4.0, 11.0], [1.0, 13.0], [4.0, 13.0]],
                [[1.0, 11.0], [4.0, 11.0], [1.0, 13.0], [4.0, 13.0]],
            ]
        )
    )


def test_get_R():
    my_env = env(9.8)

    my_bike_1 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_2 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_3 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_env.set_bikes([my_bike_1, my_bike_2, my_bike_3])

    assert np.all(
        my_env.get_R()
        == np.array(
            [
                [[1.0, 11.0], [4.0, 11.0], [1.0, 13.0], [4.0, 13.0]],
                [[1.0, 11.0], [4.0, 11.0], [1.0, 13.0], [4.0, 13.0]],
                [[1.0, 11.0], [4.0, 11.0], [1.0, 13.0], [4.0, 13.0]],
            ]
        )
    )


def test_get_ms():
    my_env = env(9.8)

    my_bike_1 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_2 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_3 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_env.set_bikes([my_bike_1, my_bike_2, my_bike_3])

    assert np.all(
        my_env.get_ms()
        == np.array([[3.0, 3.0, 2.0, 2.0], [3.0, 3.0, 2.0, 2.0], [3.0, 3.0, 2.0, 2.0]])
    )


def test_get_B():
    my_env = env(9.8)

    my_bike_1 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_2 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_3 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_env.set_bikes([my_bike_1, my_bike_2, my_bike_3])

    assert np.all(
        my_env.get_B()
        == np.array(
            [
                [
                    [0.0, 1.0, 1.0, 1.0],
                    [1.0, 0.0, 1.0, 1.0],
                    [1.0, 1.0, 0.0, 1.0],
                    [1.0, 1.0, 1.0, 0.0],
                ],
                [
                    [0.0, 1.0, 1.0, 1.0],
                    [1.0, 0.0, 1.0, 1.0],
                    [1.0, 1.0, 0.0, 1.0],
                    [1.0, 1.0, 1.0, 0.0],
                ],
                [
                    [0.0, 1.0, 1.0, 1.0],
                    [1.0, 0.0, 1.0, 1.0],
                    [1.0, 1.0, 0.0, 1.0],
                    [1.0, 1.0, 1.0, 0.0],
                ],
            ]
        )
    )


def test_get_torks():
    my_env = env(9.8)

    my_bike_1 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_2 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_3 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_env.set_bikes([my_bike_1, my_bike_2, my_bike_3])

    assert np.all(
        my_env.get_torks()
        == np.array([[1.0, 1.0, 0.0, 0.0], [1.0, 1.0, 0.0, 0.0], [1.0, 1.0, 0.0, 0.0]])
    )


def test_get_init_lenghs():
    my_env = env(9.8)

    my_bike_1 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_2 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_bike_3 = Bike(
        1,
        1,
        2,
        3,
        1,
        4,
        1,
        2,
        3,
        0,
        1,
        3,
        2,
        4,
        3,
        2,
        3,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )

    my_env.set_bikes([my_bike_1, my_bike_2, my_bike_3])

    assert np.all(
        my_env.get_init_lenghs()
        == np.array(
            [
                [
                    [0.0, 3.0, 2.0, 3.60555128],
                    [3.0, 0.0, 3.60555128, 2.0],
                    [2.0, 3.60555128, 0.0, 3.0],
                    [3.60555128, 2.0, 3.0, 0.0],
                ],
                [
                    [0.0, 3.0, 2.0, 3.60555128],
                    [3.0, 0.0, 3.60555128, 2.0],
                    [2.0, 3.60555128, 0.0, 3.0],
                    [3.60555128, 2.0, 3.0, 0.0],
                ],
                [
                    [0.0, 3.0, 2.0, 3.60555128],
                    [3.0, 0.0, 3.60555128, 2.0],
                    [2.0, 3.60555128, 0.0, 3.0],
                    [3.60555128, 2.0, 3.0, 0.0],
                ],
            ]
        )
    )


test_evalute()

test_calculate_distance_from_ground()


test_get_distance_unit_vector()


# test_get_init_lenghs()

test_get_K()