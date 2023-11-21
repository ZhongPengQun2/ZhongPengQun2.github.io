##### 方法，一个配置文件弄大而全的

- kubectl describe resourcequota -n $namespace

- apiVersion: rbac.authorization.k8s.io/v1
    - https://kubernetes.io/docs/reference/access-authn-authz/rbac/
    - kube-apiserver --authorization-mode=Example,RBAC --other-options --more-options
        - `To enable RBAC, start the API server with the --authorization-mode flag set to a comma-separated list that includes RBAC; for example:`
    - /Users/vzhong/ZhongPengQun2.github.io/docs/assets/rolebiding_serviceaccount_and_role-1024x551.webp


```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: osx:service-account
  namespace: osx-beta
rules:
- apiGroups:
  # "" indicates the core API group, '' indicates the resources belong to the core(also called legacy)API group. Example Pod, Namespaces etc below to the core api group
  # You can use kubectl api-resources -o wide to see the api resources available in your Kubernetes cluster
  # The apiGroup for deployment is apps (will vary depending on the Version of K8S you are using)
  - ""
  resources:
  - configmaps
  - pods
  - services
  - persistentvolumeclaims
  verbs:
  - get
  - list
  - watch
  - create
  - update
  - patch
  - delete
- apiGroups:
  - ""
  resources:
  - pods/exec   # 
  verbs:
  - create
- apiGroups:
  - "apps"      # 
  resources:
  - deployments
  - statefulsets
  verbs:
  - get
  - list
  - watch
  - create
  - update
  - patch
  - delete
```

ingress.yaml ↓
```
# Using shared Ingress instead of the dedicated AVI-based Ingress for now
# https://vmware.slack.com/archives/C2DE54M8F/p1644282707091739?thread_ts=1644273847.776599&cid=C2DE54M8F
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: osm
  annotations:
    kubernetes.io/ingress.class: nginx-l4-int
    nginx.ingress.kubernetes.io/proxy-body-size: 6g
spec:
  tls:
  - hosts:
    - osm-beta.eng.vmware.com
    secretName: eng-cert
  rules:
    - host: osm-beta.eng.vmware.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: osm
                port:
                  number: 80
    - host: osm-beta.vdp-stg.oc.vmware.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: osm
                port:
                  number: 80
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mailhog
  annotations:
    kubernetes.io/ingress.class: nginx-l4-int
spec:
  rules:
    - host: osm-mailhog-beta.vdp-stg.oc.vmware.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: mailhog-svc
                port:
                  number: 8025
```