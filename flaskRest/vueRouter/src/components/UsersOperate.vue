<template>
    <div>
        <div class="form-group row">
            <label for="username" class="col-sm-2 col-form-label">用户姓名 :</label>
            <div class="col-sm-10">
                <input id="username" class="form-control" type="text" v-model="username">
            </div>
        </div>
        <div class="form-group row">
            <label for="userage" class="col-sm-2 col-form-label">用户年龄 :</label>
            <div class="col-sm-10">
                <input id="userage" class="form-control" type="number" v-model="userage">
            </div>
        </div>
        <br>
        <div id="btns">
            <label class="col-sm-2"></label>
            <button class="btn btn-success" type="button" v-on:click="adduser">添加</button>
            <button class="btn btn-success" type="button" v-on:click="updateuser">更新</button>
            <button class="btn btn-success" type="button" v-on:click="deleteuser">删除</button>
            <button class="btn btn-success" type="button" v-on:click="getusers">查询</button>
        </div>
        <hr>
        <table class="table table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th>用户姓名</th>
                        <th>用户年龄</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(user, index) in users" :key="index">
                        <td v-text="user.name"></td>
                        <td v-text="user.age"></td>
                    </tr>
                </tbody>
            </table>
    </div>
</template>
<script>
    import axios from 'axios'
    // import UserList from './UserList.vue'
    export default {
        // comments:UserList,
        data() {
            return {
                username: 'xzl',
                userage: 40,
                users: []
            }
        },
        created: function () {
            const self = this;
            const path = 'http://localhost:5000/users';
            axios.get(path).then(function (res) {
                self.users = res.data;
            });
        },
        methods: {
            adduser: function () {
                const self = this;//防止username指向html元素
                const path = 'http://localhost:5000/add';
                axios.post(path, {
                    name: self.username,
                    age: self.userage
                }).then(function (res) {
                    self.users = res.data;
                })
            },
            updateuser: function () {
                const self = this;//防止username指向html元素
                const path = 'http://localhost:5000/update';
                axios.put(path, {
                    name: self.username,
                    age: self.userage
                }).then(function (res) {
                    self.users = res.data;
                })
            },
            deleteuser: function () {
                const self = this;//防止username指向html元素
                const path = 'http://localhost:5000/delete/';
                axios.delete(path + self.username
                ).then(function (res) {
                    self.users = res.data;
                })
            },
            getusers: function () {
                const self = this;
                const path = 'http://localhost:5000/users/';
                axios.get(path + self.username).then(function (res) {
                    self.users = res.data;
                })

            }
        }
    }
</script>
<style>
    tr>th,
    td {
        text-align: center;
        border: solid 1px;
    }

    #btns>button {
        margin-left: 10px;
    }
</style>