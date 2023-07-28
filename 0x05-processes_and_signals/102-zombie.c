#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Description: This function runs an infinite while loop, causing the program
 *              to keep running indefinitely.
 *
 * Return: Always returns 0.
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
 * main - Create five zombie processes.
 *
 * Description: This function creates five zombie processes using fork(). Each
 *              child process becomes a zombie by immediately exiting, while
 *              the parent process displays the PID of each zombie process
 *              created.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	pid_t child_pid;
	int zombie_count = 0;

	while (zombie_count < 5)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
			zombie_count++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}

