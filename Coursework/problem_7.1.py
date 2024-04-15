from shortest_path import shortest_path_search


def is_goal(state):
    return state == (6, 0)


start_state = (0, 0)


def successors(X, Y):
    def sc(state):
        x, y = state
        assert x <= X and y <= Y
        # res = dict()
        # res[(X, y)]: 'fill x'
        # res[(x, Y)]: 'fill y'
        # res[(0, y)]: 'empty x'
        # res[(x, 0)]: 'empty y'
        # return res
        return {
            (X, y): 'fill x',
            (x, Y): 'fill y',
            (0, y): 'empty x',
            (x, 0): 'empty y',
            (0, y + x) if y + x <= Y else (x - (Y - y), Y): 'x->y',
            (x + y, 0) if x + y <= X else (X, y - (X - x)): 'x<-y',
        }
    return sc


if __name__ == '__main__':
    res = shortest_path_search(start_state, successors(418, 986), is_goal())
    print(res)
    print('%s transitions' % (int(len(res) / 2)))
