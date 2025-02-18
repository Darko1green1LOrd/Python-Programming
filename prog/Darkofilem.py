class darkof:
    import os

    def save(filevar,text,overwrite=True,onlynew=False):
        if darkof.os.path.isdir(filevar):darkof.os.rmdir(filevar)
        if overwrite and not onlynew:
            with open(filevar, 'w') as f:
                f.writelines(text)
        elif not overwrite and not onlynew:
            with open(filevar, 'a') as f:
                f.writelines(text)
        elif onlynew and not darkof.os.path.exists(filevar):
            with open(filevar, 'w') as f:
                f.writelines(text)

    def read(filevar):
        if darkof.os.path.isdir(filevar):darkof.os.rmdir(filevar)
        if darkof.os.path.exists(filevar):
            with open(filevar, 'r') as f:
                lines = [line.strip() for line in f]
                return lines
        else:raise Exception(f"{filevar} Doesnt Exist.")

    def delete(filevar):
        if darkof.os.path.isdir(filevar):darkof.os.rmdir(filevar)
        if darkof.os.path.exists(filevar):darkof.os.remove(filevar)
