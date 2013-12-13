# {{index .Doc .Api.active.name "desc"}}
#{{with $data := .}}{{call .Fnc.counter.start}}{{range .Api.active.args}}
# {{.}} - {{index $data.Doc $data.Api.active.name "args" (call $data.Fnc.counter.value)}}{{end}}{{end}}
class {{call .Fnc.camelize .Api.active.name}}():
{{define "bodyorquery"}}{{if (eq (or (index . "method") "get") "get")}}query{{else}}body{{end}}{{end}}
	def __init__(self, {{call .Fnc.args.python .Api.active.args false}}client):{{range .Api.active.args}}
		self.{{.}} = {{.}}{{end}}
		self.client = client
{{with $data := .}}{{range .Api.active.methods}}
	# {{index $data.Doc $data.Api.active.name . "desc"}}
	# '{{index $data.Api.class $data.Api.active.name . "path"}}' {{call $data.Fnc.upper (or (index $data.Api.class $data.Api.active.name . "method") "get")}}
	#{{with $method := .}}{{call $data.Fnc.counter.start}}{{range (index $data.Api.class $data.Api.active.name $method "params")}}
	# {{.}} - {{index $data.Doc $data.Api.active.name $method "params" (call $data.Fnc.counter.value)}}{{end}}{{end}}
	def {{call $data.Fnc.underscore .}}(self, {{call $data.Fnc.args.python (index (index $data.Api.class $data.Api.active.name .) "params") false}}options = {}):
		body = options['{{template "bodyorquery" (index $data.Api.class $data.Api.active.name .)}}'] if '{{template "bodyorquery" (index $data.Api.class $data.Api.active.name .)}}' in options else {}{{range (index $data.Api.class $data.Api.active.name . "params")}}
		body['{{.}}'] = {{.}}{{end}}

		body, status, headers = self.client.{{or (index $data.Api.class $data.Api.active.name . "method") "get"}}('{{call $data.Fnc.path.python (index $data.Api.class $data.Api.active.name . "path") $data.Api.active.args}}', body, options)

		return (body, headers)
{{end}}{{end}}