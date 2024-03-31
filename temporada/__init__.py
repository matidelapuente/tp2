def goleador(data):
    """Finds the top scorer of the season.
    Args:
        data(list): contains tuples with name, goals, goals avoided and assists of each player 
        at the end of the season.
    Returns:
        tuple: contains name, goals, goals avoided and assists of the top scorer"""
    
    top_scorer = max(data, key = lambda player : player[1])
   
    return top_scorer

def puntaje(player):
    """Calculates the weighted score of the plyer.
    Args:
        player(tuple): contains name, goals, goals avoided and assists of the player.
    Returns:
        double: weighted score"""
    
    return 1.5*player[1] + 1.25*player[2] + player[3]

def influyente(data):
    """Finds the most influential player of the season.
    Args:
        data(list): contains tuples with name, goals, goals avoided and assists of each player 
        at the end of the season.
    Returns:
        tuple: contains name, goals, goals avoided and assists of the top scorer"""
    
    influential = max(data, key = lambda player : puntaje(player))
   
    return influential