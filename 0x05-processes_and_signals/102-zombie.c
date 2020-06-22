#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while- infinite loop
 * Return: Sucess
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - create 5 zombie process
 * Return: Success
 */
int main(void)
{
	pid_t pid;
	int zombie = 0;

	while (zombie < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d/n", pid);
			zombie++;
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
