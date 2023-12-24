function solution(polynomial) {
    let ports = polynomial.split(" + ")
    let linear = 0, constant = 0
    
    for (let i = 0; i < ports.length; i++){
        if(ports[i].includes("x")){
            ports[i] = ports[i].split("x")
            linear += ports[i][0] ? Number(ports[i][0]) : 1
        }
        else{
            constant += Number(ports[i])
        }
    }
    linear = linear > 1 ? linear + "x" : linear === 1 ? "x" : ""
    constant = constant ? constant : ""
    
    return linear && constant ? `${linear} + ${constant}` : `${linear}${constant}`
}