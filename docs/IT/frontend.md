npm i
    - npm install

npm run build:prod
    - 读取package.json文件

node 与 webpack 与 angular的关系
    - Angular Cli 依赖webpack，简化创建项目流程；npm属于node一部分，npm 从package.json找对应的scripts执行命令
    - webpack的运行依赖于node的环境
    - 

调试时也不再是用浏览器打开静态html调试了，直接yarn serve后在本地就会形成http://localhost:xxx的标准网站结构，而且页面内容热重载，任何代码改动，页面都会自动更新。

产品发布时，也不再是各种js,css,img文件夹了，而是对各种js、vue、ts源代码进行编译打包，最后形成了一个dist文件夹，里面拥有打包混淆好鬼都没法理解的最终文件，直接扔进nginx中就能跑。

- max_old_space_size
    - is a V8 engine parameter that can be used to raise the limit of heap memory that is allowed for us to use.

- NG_CLI_ANALYTICS=ci
    - script circle ci to disable it, if the analytics prompt blocking the ci

- SASS_BINARY_PATH
    - sass_binary_path是一个可选的设置，用于指定node-sass要使用的本地二进制文件的路径,如果没有设置sass_binary_path，node-sass会自动下载并编译本地的二进制文件。


```
node: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.28' not found (required by node)


```

# Angular
- angular vs angularJs
- What's the relationship between angular and Typescript ?

# Typescript
- online playground https://www.typescriptlang.org/play


- .component.ts
    - `.ts` 文件
        - ts 应该是表示 typescript

- npm install


```
Error from chokidar (/xxx/yyy): Error: ENOSPC: System limit for number of file watchers reached, watch '/hxxx/favicon.ico'

s:

$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
```

```
Error: ENOENT: no such file or directory, scandir '/home/hartron/foodnetteam/codebase/mandi/node_modules/node-sass/vendor'

s:

$ npm rebuild node-sass
```

- subscribe

- ===

- ngOnInit
    - ngOnInit()在angular第一次显示数据绑定和设置指令/组件的输入属性之后，初始化指令/组件

- implements OnInit {
    - x

export interface Itest
{
 exampleValue?: string; // optional
 neededValue: string; // non-optional
}
    - ?:
        - ternary operator （三元运算符)

- Install ng
```
sudo npm install -g @angular/cli
```


"Yarn 是为了弥补 npm 的一些缺陷而出现的"

- placeholder: 'Yes'
    - 当用户还没有输入值的时候,向用户显示默认的描述性说明或提示信息

- filterType: 'singleValue'
    - dropdown ？

- dependency injection

- node_modules
    - `You can think of the node_modules folder like a cache for the external modules that your project depends upon`

- .bowerrc
    - 

- EditorConfig

- eslintrc
    - `ESLint is a static code analysis tool for identifying problematic patterns found in JavaScript code.`

- angular.json

- package-lock.json & package.json
    - 默认，当我们在一个项目中npm install时候（前提该项目有package.json文件），安装完成后，会自动生成一个package-lock.json文件（位置和之前的package.json文件同级）
    - 该文件里面记录了package.json依赖的模块，以及依赖的依赖
    - 如果你有浏览它，会发现它长得类似package.json的依赖，但是比它复杂多了

- dependencies & devDependencies
    - devDependencies下列出的模块，是我们开发时用的依赖项，像一些进行单元测试之类的包，比如jest，我们用写单元测试，它们不会被部署到生产环境。dependencies下的模块，则是我们生产环境中需要的依赖，即正常运行该包时所需要的依赖项。
    - 后面的package-lock.json 中的 dependencies 对应的就是package.json中的 dependencies


- @angular/cli
    - `在使用 Angular CLI 之前，你必须确保系统中 Node.js 的版本高于 6.9.0 且 npm 的版本高于 3.0.0。`
        - node.js 与 angular的关系 ？
            - 与AngularJS不同，NodeJS是一个服务器端框架
        - npm 与 angular/cli的关系 ？
            - npm 安装 angular/cli  `npm i @angular/cli –save-dev`
            - NPM contains and manages many packages and modules, and NG is one such module
            - You can start, load compile your app using npm which internally use or load ng module if it is an angular projec

    - 安装完成后用 `$ ng version` 查看是否安装成功

- karma.conf.js

- tsconfig.spec.json

- <router-outlet></router-outlet>

- app.module.ts
    - APPMODULE: THE ROOT MODULE; Tell Angular how to construct and bootstrap the app in the root "AppModule".
        - https://v2.angular.io/docs/ts/latest/guide/appmodule.html
