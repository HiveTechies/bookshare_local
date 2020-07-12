# Books
-   APIs Listed
    -   /book/api/create/
        -   Required:
            -   To be authenticated
        -   Requires:
            -   Name of book
            -   ISBN number of book
            -   Author ID (Generally logged in user or under request)
    -   /book/api/search/
        -   Required:
            -   To be authenticated
        - Params:
            -   search
        - Usage:
            -   Either by name of book or
            -   Name of author
            -   A given tag name
    -   /book/api/view/
        -   Required:
            -   To be authenticated

# User
-   auth/token/login
    -   Requires:
        -   username
        -   password
-   auth/token/logout
-   auth/users/me
    -   Returns current user detail
-   auth/users/
    -   POST:
        -   Registers New user using username and password
    -   GET:
        -   Retrieves all the users

# Blog
    

# Friendship