function goBack() {
    window.history.back(); // 返回上一頁
  }
function postData(url, data){
    return fetch(url,{
        body:JSON.stringify(data),
        cache:'no-cache',
        credentials:'same-origin',
        headers:{
            'user-agent':'Example'
            'content-type':'application.json'
        },
        method:'POST', //GET, POST, PUT, DELETE, etc.
        mode:'cors', //no-cors, cors, same-origin
        redirect:'follow' //manual, folloe, error
        referrer:'no-referrer', //client, no-referrer
    })
        .then(response => response.json()) //輸出成json
}

function submit(){
    const quention = document.getElementById('quention').ariaValueMax;
    
}