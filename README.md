# code-templater
I called it code-templater because I used it for templating repetitive Java code that couldn't be done with a function, but you could use it for any text.

This is a solution I cooked up to Java not having proper preprocessor macros like C. Sometimes you just have to write some repetitive code and you can't turn it into a function, this hopes to make that process a little easier.

Read from the template file, replace all instances of <VAR> with lines from the arg file, in the same order.
  
  
#### Sample argument file:
    GET_INSTALLED_APPLICATIONS
    new ArrayList<ApplicationInfo>
    GET_INSTALED_PACKAGES
    new ArrayList<PackageInfo>
    ...

#### Sample template file:
    public static void generate_<VAR>() {
        return <VAR>;
    }

#### Sample output:
    public static void generate_GET_INSTALLED_APPLIATIONS() {
    	return new ArrayList<ApplicationInfo>
    }
    public static void generate_GET_INSTALLED_PACKAGES() {
    	return new ArrayList<PackageInfo>
    }
