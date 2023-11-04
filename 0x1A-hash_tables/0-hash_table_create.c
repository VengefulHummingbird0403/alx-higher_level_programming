#include "hash_tables.h"

/**
 * hash_djb2 - hashing function based on the djb2 algorithm
 * @key: the input  key
 * Return: the resulting hash value, which serves as the index
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
}hash_djb2
