# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    user_history = {}

    for site, user in zip(site_list, user_list):
        if user not in user_history:
            user_history[user] = set()

        user_history[user].add(site)

    affinities = {}
    for user, history in user_history.items():
        history = list(history)
        history.sort()
        for i, site1 in enumerate(history):
            for site2 in history[i+1:]:
                pair = (site1, site2)
                if pair not in affinities:
                    affinities[pair] = 0
                affinities[pair] += 1

    return max(affinities, key=affinities.get)

def useless():
    num_lines = 10000
    num_users = 1000

    site_list = randomized_input.randomized_site_list(num_lines)
    user_list = randomized_input.randomized_user_list(num_lines, num_users)
    time_list = range(0, num_lines)

    computed_result = compute_highest_affinity.highest_affinity(
        site_list, user_list, time_list)
    expected_result = ("facebook", "google")

    assert computed_result == expected_result
    print("Successfully passed {}!".format(os.path.basename(__file__).split(".")[0]))

def useless2():
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"
    h = "h"

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"

    user_list = [
        A, C, H, A, C, D, E, F, G, C, D, E, F, G, H, C, B, D, E, F, G, C, G, A, D,
        E, H, A, C, E, H
    ]
    site_list = [
        a, a, a, b, b, b, b, b, b, c, c, c, c, c, c, d, e, e, e, e, e, f, f, g, g,
        g, g, h, h, h, h
    ]

    time_list = range(0, 31)

    computed_result = compute_highest_affinity.highest_affinity(
        site_list, user_list, time_list)
    expected_result = (b, c)

    assert computed_result == expected_result
    print("Successfully passed {}!".format(os.path.basename(__file__).split(".")[0]))

