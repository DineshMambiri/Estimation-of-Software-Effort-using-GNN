from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route('/estimate')
def estimate():
    ems = {
        'acap' : [1.46,	1.19, 1.00, 0.86, 0.71], 
        'pcap' : [1.42, 1.17, 1.00, 0.86, 0.70], 	
        'aexp' : [1.29, 1.13, 1.00, 0.91, 0.82],   
        'modp' : [1.24, 1.10, 1.00, 0.91, 0.82], 
        'tool' : [1.24,	1.10, 1.00,	0.91, 0.83], 
        'vexp' : [1.21,	1.10, 1.00,	0.90],  	  		
        'lexp' : [1.14,	1.07, 1.00,	0.95],  	  		
        'sced' : [1.23,	1.08, 1.00,	1.04, 1.10], 	  
        'stor' : [1.00, 1.06, 1.21, 1.56], 	
        'data' : [0.94,	1.00, 1.08,	1.16], 		
        'time' : [1.00, 1.11, 1.30, 1.66], 	
        'turn' : [0.87, 1.00, 1.07, 1.15],    		
        'virt' : [0.87, 1.00, 1.15, 1.30],    	
        'rely' : [0.75, 0.88, 1.00, 1.15, 1.40],		
        'cplx' : [0.70, 0.85, 1.00, 1.15, 1.30, 1.65]
    } 
    ksloc_input = float(request.args['kloc'])
    dev_mode = request.args['mode']
    eaf = 1.0
    for em in ems.keys():
        eaf = eaf*ems[em][int(request.args[em])]
    if dev_mode == 'embedded':
        effort = 3.6*(float(ksloc_input)**1.20)*eaf
        tdev = 2.5*(effort**0.32)
    elif dev_mode == 'organic':
        effort = 2.4*(ksloc_input**1.05)
        tdev = 2.5*(effort**0.38)
    else:
        effort = 3.0*(ksloc_input**1.12)
        tdev = 2.5*(effort**0.35)
    return render_template('test.html', effort=round(effort, 2), tdev=round(tdev, 2))

if __name__ == "__main__":
    app.run()
