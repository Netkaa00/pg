from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
                
        row, col = self.position
        if self.color == 'white':
            moves = (row + 1, col)
            

        if self.color == 'black':
            moves = (row + 1, col)

        final_moves = []
        if self.is_position_on_board(moves):
            final_moves.append(moves)
        return final_moves 
        
              
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):

        row, col = self.position
        final_moves = []

        moves = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
                 ]
        
        for m_row, m_col in moves:
           r = m_row + row
           c = m_col + col

           while self.is_position_on_board((r, c)):

                final_moves.append((r, c))
                r += m_row
                c += m_col

        return final_moves



    def __str__(self):
         return f"Bishop({self.color}) at position {self.position}"
        
    
    


class Rook(Piece):
    def possible_moves(self):

        row, col = self.position
        final_moves = []

        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
                 ]
        
        for m_row, m_col in moves:
           r = m_row + row
           c = m_col + col

           while self.is_position_on_board((r, c)):

                final_moves.append((r, c))
                r += m_row
                c += m_col

        return final_moves

    def __str__(self):
        return f"Rook({self.color}) on position {self.position}"  
    


class Queen(Piece):

    def possible_moves(self):

        row, col = self.position
        final_moves = []

        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
                 ]
        
        for m_row, m_col in moves:
           r = m_row + row
           c = m_col + col

           while self.is_position_on_board((r, c)):

                final_moves.append((r, c))
                r += m_row
                c += m_col

        return final_moves
    
    def __str__(self):
        return f"Queen({self.color}) on position {self.position}"


class King(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = [
            (row - 1, col), (-1, col - 1), (row, col - 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col +1),
            (row, col + 1), (row - 1, col + 1)
        ]
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())

    piece = Pawn("white", (2, 2))
    print(piece)
    print(piece.possible_moves())

    piece = Bishop("white", (1, 2))
    print(piece)
    print(piece.possible_moves())

    piece = Rook("white", (1, 8))
    print(piece)
    print(piece.possible_moves())


    piece = Queen("white", (1, 4))
    print(piece)
    print(piece.possible_moves())


    piece = King("white", (1, 5))
    print(piece)
    print(piece.possible_moves())

