#include <stdio.h>
int main(void)
{
	int i = 0;
	int x = 4;

	while (i < x)
	{
		int j = 0;
		while (j < x)
		{
			printf("hello");
			j++;
		}
		i++;
		printf("\n");
	}
	return (0);
}
