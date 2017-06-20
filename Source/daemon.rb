require 'watir-webdriver'
require 'headless'
headless = Headless.new
headless.start
browser = Watir::Browser.new :firefox
action = false
while 1 != 0
  sleep 0.1
#  comport = open("/home/giers/talk/pythonruby.xml", 'r+')
#  comport = open("/home/giers/talk/pythonruby.xml", "r+:UTF-8")
  comport = open("pythonruby.xml", File::RDWR)
  s = comport.read
  p "Ruby: Warten auf XML.."
  state = s <=> "0"
  if state != 0
    p "Ruby: Habe String erhalten" + s
    comport.truncate(0)
    comport.seek(0)
    comport.write("0")
    success = false
    while ! success
      begin
        browser.goto "about:mozilla"
        p "Ruby: Browser läuft"
        browser.goto "https://translate.google.com/#de/en/" + s
        p "Ruby: Bin auf Google"
        browser.div(:id => 'gt-src-listen').wait_until_present
        browser.div(:id => 'gt-src-listen').click
        success = true
        #target = open("/home/giers/talk/data/talk_bool.xml", 'w')
        #target.truncate(0)
        #target.write("0")
        #p "Ruby: Resette Stuff..."
        #target.close
        comport.close
      rescue
        browser.refresh
      end
    end
  end
  comport.close
end
browser.close
headless.destroy
exit
