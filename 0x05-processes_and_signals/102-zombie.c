#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * create_zombie - Creates 5 zombie processes.
 * Description: This function forks 5 child processes, making each process
 * become a zombie by immediately exiting. The parent process prints the child
 * PID for each zombie process created.
 */
void create_zombie(void)
{
	pid_t child_pid;

	for (int i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == 0)
		{
			/* Child process */
			exit(0);
		}
		else if (child_pid > 0)
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			/* Fork failed */
			perror("fork");
			exit(1);
		}
	}
}

/**
 * infinite_while - Keeps the parent process running indefinitely.
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
 * main - Entry point of the program.
 * Return: Always returns 0.
 */
int main(void)
{
	create_zombie();
	infinite_while();
	return (0);
}

