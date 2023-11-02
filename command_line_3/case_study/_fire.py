# using fire library to access methods in an
# existing Python script from the command line

import fire
from fire_sample import Script

if __name__ == "__main__":
    fire.Fire(Script)
