# Reference
## control
<details><summary><code>client.Control.AuthSet(ProviderID, request) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set authentication credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.AuthSetRequest{
        ProviderID: "providerID",
        Body: &sdk.Auth{
            Oauth: &sdk.OAuth{
                Refresh: "refresh",
                Access: "access",
                Expires: 1,
            },
        },
    }
client.Control.AuthSet(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**providerID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `*sdk.Auth` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Control.AuthRemove(ProviderID) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove authentication credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.AuthRemoveRequest{
        ProviderID: "providerID",
    }
client.Control.AuthRemove(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**providerID:** `string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## global
<details><summary><code>client.Global.Health() -> *sdk.GlobalHealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get health information about the OpenCode server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
client.Global.Health(
        context.TODO(),
    )
}
```
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Global.Event() -> sdk.GlobalEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribe to global events from the OpenCode system using server-sent events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
client.Global.Event(
        context.TODO(),
    )
}
```
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## config
<details><summary><code>client.Config.Providers() -> *sdk.ConfigProvidersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all configured AI providers and their default models.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ConfigProvidersRequest{}
client.Config.Providers(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## instance
<details><summary><code>client.Instance.Dispose() -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clean up and dispose the current OpenCode instance, releasing all resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.InstanceDisposeRequest{}
client.Instance.Dispose(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Instance.AppAgents() -> []*sdk.Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all available AI agents in the OpenCode system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.AppAgentsRequest{}
client.Instance.AppAgents(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## project
<details><summary><code>client.Project.List() -> []*sdk.Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of projects that have been opened with OpenCode.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProjectListRequest{}
client.Project.List(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Project.Current() -> *sdk.Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the currently active project that OpenCode is working with.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProjectCurrentRequest{}
client.Project.Current(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Project.Initgit() -> *sdk.Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a git repository for the current project and return the refreshed project info.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProjectInitGitRequest{}
client.Project.Initgit(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Project.Update(ProjectID, request) -> *sdk.Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update project properties such as name, icon, and commands.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProjectUpdateRequest{
        ProjectID: "projectID",
    }
client.Project.Update(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**projectID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**icon:** `*sdk.ProjectUpdateRequestIcon` 
    
</dd>
</dl>

<dl>
<dd>

**commands:** `*sdk.ProjectUpdateRequestCommands` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Project.Directories(ProjectID) -> sdk.ProjectDirectories</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List known local absolute directories for a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProjectDirectoriesRequest{
        ProjectID: "projectID",
    }
client.Project.Directories(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**projectID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## question
<details><summary><code>client.Question.List() -> []*sdk.QuestionRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all pending question requests across all sessions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.QuestionListRequest{}
client.Question.List(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Question.Reply(RequestID, request) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide answers to a question request from the AI assistant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.QuestionReplyRequest{
        RequestID: "requestID",
        Answers: []sdk.QuestionAnswer{
            []string{
                "answers",
            },
        },
    }
client.Question.Reply(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**requestID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**answers:** `[]sdk.QuestionAnswer` — User answers in order of questions (each answer is an array of selected labels)
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Question.Reject(RequestID) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reject a question request from the AI assistant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.QuestionRejectRequest{
        RequestID: "requestID",
    }
client.Question.Reject(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**requestID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## permission
<details><summary><code>client.Permission.List() -> []*sdk.PermissionRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all pending permission requests across all sessions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.PermissionListRequest{}
client.Permission.List(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Permission.Reply(RequestID, request) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve or deny a permission request from the AI assistant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.PermissionReplyRequest{
        RequestID: "requestID",
        Reply: sdk.PermissionReplyRequestReplyOnce,
    }
client.Permission.Reply(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**requestID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**reply:** `*sdk.PermissionReplyRequestReply` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## provider
<details><summary><code>client.Provider.List() -> *sdk.ProviderListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all available AI providers, including both available and connected ones.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProviderListRequest{}
client.Provider.List(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Provider.Auth() -> map[string][]*sdk.ProviderAuthMethod</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve available authentication methods for all AI providers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProviderAuthRequest{}
client.Provider.Auth(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Provider.OauthAuthorize(ProviderID, request) -> *sdk.ProviderAuthAuthorization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start the OAuth authorization flow for a provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProviderOauthAuthorizeRequest{
        ProviderID: "providerID",
        Method: 1.1,
    }
client.Provider.OauthAuthorize(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**providerID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `float64` — Auth method index
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `map[string]string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Provider.OauthCallback(ProviderID, request) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Handle the OAuth callback from a provider after user authorization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.ProviderOauthCallbackRequest{
        ProviderID: "providerID",
        Method: 1.1,
    }
client.Provider.OauthCallback(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**providerID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `float64` — Auth method index
    
</dd>
</dl>

<dl>
<dd>

**code:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## session
<details><summary><code>client.Session.List() -> []*sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all OpenCode sessions, sorted by most recently updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionListRequest{}
client.Session.List(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `*sdk.SessionListRequestScope` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**roots:** `*sdk.SessionListRequestRoots` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `*float64` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `*float64` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Create(request) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new OpenCode session for interacting with AI assistants and managing conversations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionCreateRequest{}
client.Session.Create(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**parentID:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**agent:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `*sdk.SessionCreateRequestModel` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `map[string]any` 
    
</dd>
</dl>

<dl>
<dd>

**permission:** `*sdk.PermissionRuleset` 
    
</dd>
</dl>

<dl>
<dd>

**workspaceID:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Status() -> map[string]*sdk.SessionStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the current status of all sessions, including active, idle, and completed states.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionStatusRequest{}
client.Session.Status(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Get(SessionID) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information about a specific OpenCode session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionGetRequest{
        SessionID: "sessionID",
    }
client.Session.Get(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Delete(SessionID) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a session and permanently remove all associated data, including messages and history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionDeleteRequest{
        SessionID: "sessionID",
    }
client.Session.Delete(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Update(SessionID, request) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update properties of an existing session, such as title or other metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionUpdateRequest{
        SessionID: "sessionID",
    }
client.Session.Update(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `map[string]any` 
    
</dd>
</dl>

<dl>
<dd>

**permission:** `*sdk.PermissionRuleset` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `*sdk.SessionUpdateRequestTime` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Children(SessionID) -> []*sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all child sessions that were forked from the specified parent session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionChildrenRequest{
        SessionID: "sessionID",
    }
client.Session.Children(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Todo(SessionID) -> []*sdk.Todo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the todo list associated with a specific session, showing tasks and action items.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionTodoRequest{
        SessionID: "sessionID",
    }
client.Session.Todo(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Diff(SessionID) -> []*sdk.SnapshotFileDiff</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the file changes (diff) that resulted from a specific user message in the session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionDiffRequest{
        SessionID: "sessionID",
    }
client.Session.Diff(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Messages(SessionID) -> []*sdk.SessionMessagesResponseItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all messages in a session, including user prompts and AI responses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionMessagesRequest{
        SessionID: "sessionID",
    }
client.Session.Messages(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `*int` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Prompt(SessionID, request) -> *sdk.SessionPromptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and send a new message to a session, streaming the AI response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionPromptRequest{
        SessionID: "sessionID",
        Parts: []*sdk.SessionPromptRequestPartsItem{
            &sdk.SessionPromptRequestPartsItem{
                Text: &sdk.TextPartInput{
                    Text: "text",
                },
            },
        },
    }
client.Session.Prompt(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `*sdk.SessionPromptRequestModel` 
    
</dd>
</dl>

<dl>
<dd>

**agent:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**noReply:** `*bool` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `map[string]bool` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `*sdk.OutputFormat` 
    
</dd>
</dl>

<dl>
<dd>

**system:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**variant:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**parts:** `[]*sdk.SessionPromptRequestPartsItem` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Message(SessionID, MessageID) -> *sdk.SessionMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific message from a session by its message ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionMessageRequest{
        SessionID: "sessionID",
        MessageID: "messageID",
    }
client.Session.Message(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Deletemessage(SessionID, MessageID) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a specific message and all of its parts from a session without reverting file changes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionDeleteMessageRequest{
        SessionID: "sessionID",
        MessageID: "messageID",
    }
client.Session.Deletemessage(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Fork(SessionID, request) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new session by forking an existing session at a specific message point.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionForkRequest{
        SessionID: "sessionID",
    }
client.Session.Fork(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Abort(SessionID) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Abort an active session and stop any ongoing AI processing or command execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionAbortRequest{
        SessionID: "sessionID",
    }
client.Session.Abort(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Init(SessionID, request) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze the current application and create an AGENTS.md file with project-specific agent configurations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionInitRequest{
        SessionID: "sessionID",
        ModelID: "modelID",
        ProviderID: "providerID",
        MessageID: "messageID",
    }
client.Session.Init(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**modelID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**providerID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Share(SessionID) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a shareable link for a session, allowing others to view the conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionShareRequest{
        SessionID: "sessionID",
    }
client.Session.Share(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Unshare(SessionID) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the shareable link for a session, making it private again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionUnshareRequest{
        SessionID: "sessionID",
    }
client.Session.Unshare(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Summarize(SessionID, request) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a concise summary of the session using AI compaction to preserve key information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionSummarizeRequest{
        SessionID: "sessionID",
        ProviderID: "providerID",
        ModelID: "modelID",
    }
client.Session.Summarize(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**providerID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**modelID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**auto:** `*bool` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.PromptAsync(SessionID, request) -> error</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and send a new message to a session asynchronously, starting the session if needed and returning immediately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionPromptAsyncRequest{
        SessionID: "sessionID",
        Parts: []*sdk.SessionPromptAsyncRequestPartsItem{
            &sdk.SessionPromptAsyncRequestPartsItem{
                Text: &sdk.TextPartInput{
                    Text: "text",
                },
            },
        },
    }
client.Session.PromptAsync(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `*sdk.SessionPromptAsyncRequestModel` 
    
</dd>
</dl>

<dl>
<dd>

**agent:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**noReply:** `*bool` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `map[string]bool` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `*sdk.OutputFormat` 
    
</dd>
</dl>

<dl>
<dd>

**system:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**variant:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**parts:** `[]*sdk.SessionPromptAsyncRequestPartsItem` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Command(SessionID, request) -> *sdk.SessionCommandResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a new command to a session for execution by the AI assistant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionCommandRequest{
        SessionID: "sessionID",
        Arguments: "arguments",
        Command: "command",
    }
client.Session.Command(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**agent:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**arguments:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**command:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**variant:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**parts:** `[]*sdk.SessionCommandRequestPartsItem` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Shell(SessionID, request) -> *sdk.SessionShellResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a shell command within the session context and return the AI's response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionShellRequest{
        SessionID: "sessionID",
        Agent: "agent",
        Command: "command",
    }
client.Session.Shell(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**agent:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `*sdk.SessionShellRequestModel` 
    
</dd>
</dl>

<dl>
<dd>

**command:** `string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Revert(SessionID, request) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revert a specific message in a session, undoing its effects and restoring the previous state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionRevertRequest{
        SessionID: "sessionID",
        MessageID: "messageID",
    }
client.Session.Revert(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**partID:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.Unrevert(SessionID) -> *sdk.Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore all previously reverted messages in a session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.SessionUnrevertRequest{
        SessionID: "sessionID",
    }
client.Session.Unrevert(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.PermissionRespond(SessionID, PermissionID, request) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve or deny a permission request from the AI assistant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.PermissionRespondRequest{
        SessionID: "sessionID",
        PermissionID: "permissionID",
        Response: sdk.PermissionRespondRequestResponseOnce,
    }
client.Session.PermissionRespond(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**permissionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**response:** `*sdk.PermissionRespondRequestResponse` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.PartDelete(SessionID, MessageID, PartID) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a part from a message.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.PartDeleteRequest{
        SessionID: "sessionID",
        MessageID: "messageID",
        PartID: "partID",
    }
client.Session.PartDelete(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**partID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.Session.PartUpdate(SessionID, MessageID, PartID, request) -> *sdk.Part</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a part in a message.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.PartUpdateRequest{
        SessionID: "sessionID",
        MessageID: "messageID",
        PartID: "partID",
        Body: &sdk.Part{
            Text: &sdk.TextPart{
                ID: "id",
                SessionID: "sessionID",
                MessageID: "messageID",
                Text: "text",
            },
        },
    }
client.Session.PartUpdate(
        context.TODO(),
        request,
    )
}
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sessionID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**messageID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**partID:** `string` 
    
</dd>
</dl>

<dl>
<dd>

**directory:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**workspace:** `*string` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `*sdk.Part` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

