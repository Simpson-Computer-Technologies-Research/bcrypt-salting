##
## Author:
##  @see https://stackoverflow.com/questions/43253392/how-many-rounds-is-the-recommended-for-bcrypt-password-hasing
##

##
## Libraries
##
import bcrypt, time, random, string


##
## Functions
##
def generate_random_password(length: int):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def hash_password(password: str, rounds: int):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=rounds))


##
## Main
##
def main(plength: int = 16, rounds: int = 16):
    MIN_ROUNDS: int = 4

    ##
    ## For loop to test the time it takes to hash a password
    ## depending on the number of rounds
    ##
    print("Password Length =", plength)
    for rounds in range(MIN_ROUNDS, rounds):
        password = generate_random_password(plength)

        ##
        ## Start the timer and hash the password. Afterwards, calculate the time it took
        ## to hash the password and print the results
        ##
        start = time.time()
        hash_password(password, rounds)
        end = time.time()
        seconds = end - start

        print(f"rounds={rounds} time(s)={seconds:.6f} password={password}")


##
## Execution
##
if __name__ == "__main__":
    main()
