<template>
    <div>
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
    export default {
        name: 'UserList',
        data() {
            return {
                users: [
                    {
                        name: "xzl",
                        age: 35
                    }
                ]
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
</style>