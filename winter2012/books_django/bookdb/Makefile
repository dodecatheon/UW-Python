all:	books.db

books.db:	books books_data
	-@rm $@
	echo ".quit" | sqlite3 -init script $@
