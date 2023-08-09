#ifndef ECSONAI_HPP
#define ECSONAI_HPP

#include "OthelloAI.hpp"
#include <vector>
namespace ecsonh
{
    class EcsonAI: public OthelloAI
    {
    public:
        std::pair<int, int> chooseMove(const OthelloGameState& state) override;
        int search(OthelloGameState& state, int depth, OthelloCell& myturn);
        void eval(const OthelloGameState& state, OthelloCell& turn);
        // void newsteps(const OthelloBoard& board, const OthelloGameState& state);
    private:
        //std::vector<std::pair<int,int>> steps;
        int evaluation;
    };
}

#endif
