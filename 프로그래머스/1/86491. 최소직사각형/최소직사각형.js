function solution(sizes) {
    const sizes_sort = sizes.map(([w,h]) => w > h ? [w,h] : [h,w])
    
    let wmax = 0, hmax  = 0
    sizes_sort.forEach(([w, h]) => {
        wmax = Math.max(wmax,w)
        hmax = Math.max(hmax,h)
    })
    return wmax * hmax
}

// function solution(sizes) {
// }

// function solution(sizes) {
//     const sizes_sort = sizes.map((size,index) => {
//         if (size[0] >= size[1]){return [size[0], size[1]]}
//         else if (size[0] < size[1]){return [size[1], size[0]]}
//     })
//     let lmax = 0, rmax = 0
    
//     for(let size of sizes_sort){
//         if (lmax < size[0]) { lmax = size[0]}
//         if (rmax < size[1]) { rmax = size[1]}
//     }
//     return lmax * rmax
// }

// function solution(sizes) {
//     let ans = []
//     let max_w = 0
//     let max_h = 0
//     for (let i = 0; i < sizes.length; i++){
//         let tmp = 0
//         if(sizes[i][0] > sizes[i][1]){
//             tmp = sizes[i][0]
//             sizes[i][0] = sizes[i][1]
//             sizes[i][1] = tmp
//         }
        
//         if(max_w < sizes[i][0] ) {max_w = sizes[i][0]}
//         if(max_h < sizes[i][1] ) {max_h = sizes[i][1]}
//     }
//     return max_w * max_h;
// }
