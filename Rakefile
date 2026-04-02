# frozen_string_literal: true

def production?
  ENV["JEKYLL_ENV"] == "production"
end

webpacked_js = "javascript/main.js"
installed_package_lock_json = "node_modules/.package-lock.json"
js_dependency_files = ["package.json"]
lockfiles = ["package-lock.json", "npm-shrinkwrap.json", "yarn.lock", "pnpm-lock.yaml"]
js_dependency_files.concat(lockfiles.select { |file| File.exist?(file) })

file installed_package_lock_json => js_dependency_files do
  if production?
    sh("npm", "ci")
  else
    sh("npm", "install", "--no-save")
  end
end

file webpacked_js => ["_webpack/main.js", installed_package_lock_json] do
  rm_f(webpacked_js)
  command_line = ["npx", "webpack"]
  command_line << "--mode=production" if production?
  sh(*command_line)
end

desc "Serve site locally"
task :serve => webpacked_js do
  command_line = ["jekyll", "serve"]
  # Incremental build can cause stale content; disable by setting JEKYLL_INCREMENTAL=false
  incremental = ENV.fetch("JEKYLL_INCREMENTAL", "true")
  command_line << "--incremental" if incremental == "true"
  command_line += ["--livereload",
                   "--host", ENV["HOST"] || "127.0.0.1"]
  sh(*command_line)
end

task :default => :serve

desc "Generate site"
task :generate => webpacked_js do
  command_line = ["jekyll", "build"]
  base_url = ENV["JEKYLL_BASE_URL"]
  command_line << "--baseurl=#{base_url}" if base_url
  extra_config = ENV["JEKYLL_EXTRA_CONFIG"]
  command_line << "--config=_config.yml,#{extra_config}" if extra_config
  destination = ENV["JEKYLL_DESTINATION"]
  command_line << "--destination=#{destination}" if destination
  sh(*command_line)
end
