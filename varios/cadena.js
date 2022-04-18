let cadena="causal=&causal=223333&causal=3&causal=";
cadenas=cadena.split("&");

valores = cadenas.map((cadenas,index,cadena)=>{
    fin =cadena[index].length
    return cadena[index].substr(7,fin);
    
})
console.log(valores.indexOf(''));