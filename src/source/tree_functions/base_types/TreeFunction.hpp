#pragma once
#include <vector>
#include "source/tree/Node.hpp"
#include "source/utilities/RandomGenerator.hpp"

namespace Mtree
{
	class TreeFunction
	{
	protected:
		RandomGenerator rand_gen;
		std::vector<std::shared_ptr<TreeFunction>> children;
		void execute_children(std::vector<Stem>& stems, int id);
	public:
		int seed = 42;

		virtual void execute(std::vector<Stem>& stems, int id=0, int parent_id = 0) = 0;
		void add_child(std::shared_ptr<TreeFunction> child);
	};
}