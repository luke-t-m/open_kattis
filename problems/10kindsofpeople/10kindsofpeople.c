#include <stdio.h>

// use: print_grid((int *)grid, height, width);
void print_grid(int *grid, int height, int width)
{
  for (int r = 0; r < height; r++)
  {
    for (int c = 0; c < width; c++)
    {
      printf("%d ", grid[r * width + c]);
    }
    printf("\n");
  }
}


int main()
{
  //input
  int height, width;
  scanf("%d%d", &height, &width);

  int grid[height][width];
  for (int r = 0; r < height; r++)
  {
    for (int c = 0; c < width; c++)
    {
      scanf("%1d", &grid[r][c]);
    }
  }
  //print_grid((int *)grid, width);

  int no_queries;
  scanf("%d", &no_queries);
  int queries[no_queries][4];
  for (int query_no = 0; query_no < no_queries; query_no ++)
  {
    for (int coord_no = 0; coord_no < 4; coord_no ++)
    {
      scanf("%d", &queries[query_no][coord_no]);
    }
  }
  //print_grid((int *)queries, no_queries, 4);

  //flood
  int lastsegs[2] = {0, 1};
  // impl. a stack or a queue or something

  for (int query_no = 0; query_no < no_queries; query_no ++)
  {
    //check if they are the same of we sned
  }








}