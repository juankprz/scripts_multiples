
let personas =[
    ['juan','perez'],
    ['andres','perez'],
    ['test','perez']
]
let edades =[
    [10],
    [20],
    [15]
]

let valores=personas.map((personas,index,persona) => {
    return [
      persona[index][0],
      persona[index][1],
      edades[index][0]
    ]
})
console.log(valores[0][1]);