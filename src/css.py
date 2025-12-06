

def css_style() -> str:
    return """
    #main {
        width: 100%;
        height: 100%;
    }   

    #title {
        width: 100%;
        height: 50%;
        content-align: center middle;
        text-align: center
    }


    #btn_group {
        width: 100%;
        height: 50%;
        background-tint:blue 10%;
        align: center top;

    }

    #start {
        min-width: 10;
        width: 50%;
        margin-right: 2;
        max-width: 30;
        background: #2b14d7ca;
    }

    #start:hover {
        background: #120d3aca;
    }

    #stop {
        width: 20;
        width: 50%;
        min-width: 10;
        max-width: 30;
        background: #DE1A58;

    }

    #stop:hover {
        background: #DE1A58;
        text-style: bold;
    }

    """