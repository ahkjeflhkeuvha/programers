function solution(num_list) {
    var odd = 0, even = 0;
    for(i in num_list){
        if(i%2 == 0) odd += num_list[i]
        else even += num_list[i]
    }
    return odd > even ? odd : even
}