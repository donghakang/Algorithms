BFS(G, s)
    for each vertex u in G. V - {s}
        u.color = white
        u.d = Inf
        u.pi = NIL
    s.color = Gray
    s.d = 0
    s.pi = NIL

    Q = {}
    Enqueue(Q,s)

    # til here it is step A
    while Q != {}
        u = Dequeue(Q)
        for each v in G.adj[u]  # means, the values where it is adjacent
            if v.color == white
                v.color = Gray
                v.d = u.d + 1
                v.pi = u
                Enqueue(Q,v)
        u.color = black
