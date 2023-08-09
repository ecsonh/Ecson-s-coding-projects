#include "EcsonAI.hpp"
#include <ics46/factory/DynamicFactory.hpp>
#include "OthelloCell.hpp"
#include "OthelloGameState.hpp"



ICS46_DYNAMIC_FACTORY_REGISTER(OthelloAI, ecsonh::EcsonAI, "EcsonAI(Required)");

std::pair<int, int> ecsonh::EcsonAI::chooseMove(const OthelloGameState& state)
{ 
    //std::vector<std::pair<int,int>>steps = newsteps(state.board(),state);
    OthelloCell current_turn;
    if(state.isWhiteTurn())
    {
        current_turn = OthelloCell::white;
    }
    else if (state.isBlackTurn())
    {
        current_turn = OthelloCell::black;
    }


    int highest_point = -1000000;
    std::pair<int, int> best;
    const OthelloBoard& board = state.board(); 
    for(int i =0; i< board.width(); i++)
    {
        for (int j = 0 ; j < board.height();j++)
        {
            if(state.isValidMove(i,j))
            {
                std::unique_ptr<OthelloGameState> newboard = state.clone();
                newboard -> makeMove(i, j);
                int point = search(*newboard, 6, current_turn);
                if(point>highest_point)
                {
                    highest_point = point;
                    best.first = i;
                    best.second = j;
                }
            }
        }

    }
    return best;
}
int ecsonh::EcsonAI::search(OthelloGameState& state, int depth, OthelloCell& myturn)
{
    OthelloCell current_turn;
    if(state.isWhiteTurn())
    {
        current_turn = OthelloCell::white;
    }
    else if(state.isBlackTurn())
    {
        current_turn = OthelloCell::black;
    }
    else
    {
        current_turn = OthelloCell::empty;
    }

    if (depth == 0 || state.isGameOver())
    {
        eval(state, current_turn);
        return evaluation;
    }
    else
    {
        const OthelloBoard& board = state.board(); 
        if(myturn == current_turn)
        {
            int max_pt = -1000000;
            for(int i =0; i< board.width(); i++)
            {
                for (int j = 0 ; j < board.height();j++)
                {
                    if(state.isValidMove(i,j)&& board.cellAt(i, j) == OthelloCell::empty)
                    {
                        std::unique_ptr<OthelloGameState> newboard = state.clone();
                        newboard -> makeMove(i, j);
                        int point = search(*newboard, depth-1, myturn);
                        if(point > max_pt)
                        {
                            return point;
                        }
                    }
                }
            }
            
        }
        else
        {
            int min_pt = 1000000;
            for(int i =0; i< board.width(); i++)
            {
                for (int j = 0 ; j < board.height();j++)
                {
                    if(state.isValidMove(i,j)&& board.cellAt(i, j) == OthelloCell::empty)
                    {
                        std::unique_ptr<OthelloGameState> newboard = state.clone();
                        newboard -> makeMove(i, j);
                        int point = search(*newboard, depth-1, myturn);
                        if(point < min_pt)
                        {
                            return point;
                        }
                    }
                }
            
            }
            
        }
    }
    return 0;
        // if it's my turn to move:
        //     for each valid move that I can make from s:
        //         make that move on s yielding a state s'
        //         search(s', depth - 1)
        //     return the maximum value returned from recursive search calls
        // else:
        //     for each valid move that my opponent can make from s:
        //         make that move on s yielding a state s'
        //         search(s', depth - 1)
        //     return the minimum value returned from recursive search calls
}
void ecsonh::EcsonAI::eval(const OthelloGameState& state, OthelloCell& turn)
{
    if(turn == OthelloCell::white) //AI play as white
    {
        evaluation = state.whiteScore()-state.blackScore();
    }
    else
    {
        evaluation = state.blackScore() - state.whiteScore();
    }

}
// void ecsonh::EcsonAI::newsteps(const OthelloBoard& board, const OthelloGameState& state)
// {
//     steps.clear();
//     int y = board.height();
//     int x = board.width();
//     for(int i =0; i< x; i++)
//     {
//         for (int j = 0 ; j < y;j++)
//         {
//             if(state.isValidMove(i,j))
//             {
//                 std::pair<int,int> s(i,j);
//                 steps.push_back(s);
//             }
//         }
//     }
//     
// }
