#include "hash_tables.h"

/**
 * hash_djb2 - This function implements the djb2 algorithm for hashing.
 * @key: the input key
 * Return: the computed hash value, which is used as the index
 */
unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hash;
	int c;

	hash = 5381;
	while ((c = *str++))
	{
		hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
	}
	return (hash);
}
