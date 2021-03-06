import nbformat, os

rootdir = ""
subdirs = ["continuous_time", "dynamic_programming", "dynamic_programming_squared", "getting_started_julia", "more_julia", "multi_agent_models", "time_series_models", "tools_and_techniques"]
assetdir = "../lecture-source-jl/source/"


colab_markdown_text = open(os.path.join(assetdir, "_static", "includes", "colab-instructions.md")).read()
colab_markdown_cell = nbformat.v4.new_markdown_cell(colab_markdown_text)

colab_code_text = open(os.path.join(assetdir, "_static", "includes", "colab_code_cell.txt")).read()
colab_code_cell = nbformat.v4.new_code_cell(colab_code_text)

for dir in subdirs:
    path = os.path.join(rootdir, dir)
    nbs = os.listdir(path)
    for nb in nbs:
        if os.path.splitext(nb)[1] == '.ipynb':
            print(os.path.join(path, nb))
            nb_dict = nbformat.read(os.path.join(path, nb), 4)
            nb_dict['cells'].insert(2, colab_markdown_cell)
            nb_dict['cells'].insert(3, colab_code_cell)
            nbformat.write(nb_dict, os.path.join(path, nb))
