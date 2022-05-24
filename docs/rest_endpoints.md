        
# V1

## users
0. POST users - creates a new user, returns user_id and session_key

### users/{user-id}
GET users/1 - returns user info with id 1

### users/{user-id}/wallets

1. POST users/admin/wallets - creates a new wallet, returns wallet_id
2. GET 	users/admin/wallets - returns all wallets
3. GET 	users/admin/wallets/1 - returns the wallet "1"   # Where does a user should retrieve ids from?

### users/{user-id}/transactions/

8. GET	users/admin/transactions - returns all transactions of admin user

### users/{user-id}/wallets/{wallet-id}/securities
GET users/admin/wallets/1/securites?filter=bonds

4. POST users/admin/wallets/1/securites/ - adds the security to the wallet "1"
5. GET 	users/admin/wallets/1/securites/  - returns all securites of the wallet "1"
6. GET	users/admin/wallets/1/securites/isin - returns the user's security by isin


9. GET	users/admin/wallets/1/transactions - returns all transactions of admin user in the wallet "1"

## transactions
10. OR	GET transactions?{user_id}&{wallet}&{security}