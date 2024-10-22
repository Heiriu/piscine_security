#include <stdio.h>

int		main()
{
	char buffer[80];
	char psw[4] = "test";

	printf("Please enter key: ");
	scanf( "%[^\n]", buffer);
	fgetc(stdin);
	for (int i = 0; i < 4; i++)
	{
		if (buffer[i] != psw[i])
		{
			printf("Nope.\n");
			return (-1);
		}
	}
	return (0);
}