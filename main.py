from RWESharp.Core.Application import Application

app: Application | None = None  # having it global so it won't get GC'ed just in case

def main():
    global app
    print(r"""
       ___ _      ______  ____ 
      / _ \ | /| / / __/_/ / /_
     / , _/ |/ |/ / _//_  . __/
    /_/|_||__/|__/___/_    __/ 
                      /_/_/    

    RWE# - timofey26, atom and lang0s
    """)
    # damn, even cleaner than before
    app = Application()


if __name__ == "__main__":
    main()
