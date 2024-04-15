from shortest_path import shortest_path_search


def is_goal(state):
    return state == [(0, 0), (3, 3)]


start_state = [(3, 3), (0, 0)]


def successors(X, Y):
    def sc(state):
        (cl, ml), (cr, mr) = state
        assert mr + ml == 3 and cr + cl == 3
        return {
            # from right to left
            [(cl - 1, ml), (cr + 1, mr)] if mr >= cr + 1 else [(cl, ml - 1), (cr, mr + 1)]: 'one to left',
            [(cl - 2, ml), (cr + 2, mr)] if mr >= cr + 2 else [(cl, ml - 2), (cr, mr + 2)]: 'two to left',
            [(cl - 1, ml - 1), (cr + 1, mr + 1)]: 'cannibal & misionary to left',

            # from left to right
            [(cl + 1, ml), (cr - 1, mr)] if ml >= cl + 1 else [(cl, ml + 1), (cr, mr - 1)]: 'one to right',
            [(cl + 2, ml), (cr - 2, mr)] if ml >= cl + 2 else [(cl, ml + 2), (cr, mr - 2)]: 'two to right',
            [(cl + 1, ml + 1), (cr - 1, mr - 1)]: 'cannibal & misionary to right',
        }

    return sc
