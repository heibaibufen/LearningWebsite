<!-- <template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li>
        <a href="https://vuejs.org" target="_blank">
          Core Docs
        </a>
      </li>
      <li>
        <a href="https://forum.vuejs.org" target="_blank">
          Forum
        </a>
      </li>
      <li>
        <a href="https://chat.vuejs.org" target="_blank">
          Community Chat
        </a>
      </li>
      <li>
        <a href="https://twitter.com/vuejs" target="_blank">
          Twitter
        </a>
      </li>
      <br>
      <li>
        <a href="http://vuejs-templates.github.io/webpack/" target="_blank">
          Docs for This Template
        </a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a href="http://router.vuejs.org/" target="_blank">
          vue-router
        </a>
      </li>
      <li>
        <a href="http://vuex.vuejs.org/" target="_blank">
          vuex
        </a>
      </li>
      <li>
        <a href="http://vue-loader.vuejs.org/" target="_blank">
          vue-loader
        </a>
      </li>
      <li>
        <a href="https://github.com/vuejs/awesome-vue" target="_blank">
          awesome-vue
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted() {
    axios({
      method: "POST",
      url: "/UserInfo",
      data: {
        username: "4",
        password: "4"
      }

    }).then(res => {
      console.log(res);
    })
  }
}
</script> -->

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- <style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style> -->

<template>
  <div class="hello">
      <h1>{{ msg }}</h1>
      <ul>
          <li v-for="(user,index) in users" :key="index" style="display: block;">
              {{ index }}--{{ user.username }}--{{ user.password }}
          </li>
      </ul>
      <form action="">
          用户名：<input type="text" placeholder="user name" v-model="inputUser.username"><br>

          密码：<input type="text" placeholder="user password" v-model="inputUser.password"><br>
          <button type="submit" @click="userSubmit()">提交</button>
      </form>
  </div>
</template>

<script>
import { getUsers,postUser } from '../api/api.js';
export default {
  name:'hellouser',
  data () {
      return {
          msg:'Welcome to Your Vue.js App',
          users:[
              {username:'test1',password:'test1'},
              {username:'test2',password:'test2'}
          ],
          inputUser:{
              "username":"",
              "password":"",
          }
      }
  },
  methods:{
      loadUsers(){
          getUsers().then(response=>{
              this.users=response.data
          })
      },
      userSubmit(){
          postUser(this.inputUser.username,this.inputUser.password).then(response=>{
              console.log(response)
              this.loadUsers()
          })
      }
  },
  created: function(){
      this.loadUsers()
  }
}
</script>
