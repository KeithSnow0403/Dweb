<template>
  <div id="login" @click.self="hideSelf">
    <div id="loginbox">
      <div class="form">
        <div v-if="target==1 || target==2" class="item">
          <div class="span">用户名:</div>
          <input v-model="username" type="text" placeholder="请输入用户名" />
        </div>
        <div v-if="target==1 || target==2" class="item">
          <div class="span">密码:</div>
          <input v-model="password" type="text" placeholder="请输入密码" />
        </div>
        <div v-if="target==2" class="item">
          <div class="span">重复密码:</div>
          <input v-model="password2" type="text" placeholder="请再次输入密码" />
        </div>
        <div v-if="target==3" class="item">
          <div class="span">网站名称:</div>
          <input v-model="sitename" type="text" placeholder="请输入网站名称" />
        </div>
        <div v-if="target==3" class="item">
          <div class="span">图片上传:</div>
          <input id="uploadLogo" @change="uploadImg($event)" type="file" style="width:150px" />
        </div>

        <button v-if="target==1" @click="toLogin">登陆</button>
        <button v-if="target==2" @click="toRegister">注册</button>
        <button v-if="target==3" @click="toUpload">确定</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  name: "LoginBox",
  props: ["target"],
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      sitename:"",
    };
  },
  mounted() {
    console.log(this.target);
  },
  methods: {
    //登陆
    toLogin() {
      console.log(this.username, this.password);
      var username = this.username;
      var password = this.password;
      if (username.length > 0 && password.length > 0) {
        axios({
          url: "http://127.0.0.1:9000/login/",
          data: Qs.stringify({
            username,
            password,
          }),
          method: "post",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }).then((res) => {
          console.log(res);
          switch (res.data) {
            case "none":
              alert("用户名不存在");
              break;
            case "pwd_err":
              alert("密码错误");
              break;
            default:
              console.log(res.data.token);
              alert("登陆成功");
              break;
          }
        });
      } else {
        alert("用户名或密码不能为空");
      }
    },
    //注册
    toRegister() {
      var username = this.username;
      var password = this.password;
      var password2 = this.password2;
      console.log(username, password, password2);
      if (username.length > 0 && password.length > 0 && password2.length > 0) {
        if (password != password2) {
          alert("密码不一致");
        } else {
          axios({
            url: "http://127.0.0.1:9000/register/",
            data: Qs.stringify({
              username,
              password,
              password2,
            }),
            method: "post",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
          }).then((res) => {
            console.log(res);
            switch (res.data) {
              case "exist":
                alert("用户已存在");
                break;

              default:
                break;
            }
          });
        }
      } else {
        alert("用户名或密码不能为空");
      }
    },
    toUpload(){
        var sitename = this.sitename
        // var logo = document.getElementById('uploadLogo').files[0]
        console.log(sitename)
        // console.log(logo)  
    },
    uploadImg(e){
        // console.log(e)
        var logo = e.target.files[0]
        console.log(logo)
        var img = new FormData()
        img.append('logo',logo)
        axios({
            url:'http://127.0.0.1:9000/upload-logo/',
            method:'post',
            headers:{
                'Content-Type':'application/x-www-form-urlencoded'
            },
            data:img,
        }).then((res)=>{
            console.log(res)
        })
    },
    hideSelf() {
      this.$emit("hideBox");
    },
  },
  //   methods: {
  //     toLogin() {
  //       console.log(this.username,this.password);
  //       var username = this.username
  //       var password = this.password
  //       axios({
  //         url: "http://127.0.0.1:9000/login/",
  //         data: {
  //             username,
  //             password
  //         },
  //         method:'post',
  //         headers:{
  //             "Content-Type":"application/x-www-form-urlencoded"
  //         },
  //       }).then((res)=>{
  //           console.log(res)
  //       })
  //     },
  //   },
};
</script>

<style>
#login {
  position: absolute;
  top: 0;
  width: 700px;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #0002;
}

#loginbox {
  width: 300px;
  height: 300px;
  border: 1px solid #000;
  background: #0009;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
}

#loginbox .form .item {
  font-weight: 700;
  margin: 10px auto;
}

#login .form .item .span {
  float: left;
  width: 80px;
}
</style>