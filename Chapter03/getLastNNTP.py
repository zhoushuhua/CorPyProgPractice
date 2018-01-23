#
import nntplib
import socket

# defined constant var
HOST = "news.gmane.org"
GRNM = "gmane.comp.python.committers"

def displayFirst20(data):
    print "first (<=20) meaingful lines:\n"
    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True
    for line in lines:
        # if line:
        #     lower = line.lower()
        #     if (lower.startswith(">") and not \
        #             lower.startswith(">>>")) or not \
        #             lower.startswith("|") or not \
        #             lower.startswith("in article") or not \
        #             lower.endswith("writes:") or not \
        #             lower.endsswith("wrote:"):
        #         continue
        # if not lastBlank or (lastBlank and line):
        print "     %s" % line
        #     if line:
        #         count += 1
        #         lastBlank = False
        #     else:
        #         lastBlank = True
        # if count == 20:
        #     break;

def main() :
    try:
        n = nntplib.NNTP(HOST)

        #
        try:
            resp, cnt, first, last, grp = n.group(GRNM)
        except nntplib.NNTPPermanentError as e:
            print "cannot load group %s" % GRNM
            return

        rng = "%s-%s" % (first, last)
        resp, frms = n.xhdr("from", rng)
        resp, subs = n.xhdr("subject", rng)
        resp, dats = n.xhdr("date", rng)

        print """*** Found last article #(%s)

            Form:%s
            Subject:%s
            Data:%s
            """ % (last, frms[0][1], subs[0][1], dats[0][1])

        resp, num, id, list = n.body(last)
        displayFirst20(list)
    except socket.gaierror as e:
        print "Error cannot reach %s" % str(e)
    except nntplib.NNTPPermanentError as e:
        print "Error Access denied on %s" % HOST
    finally:
        if n in locals():
            n.quit()
#
if __name__  == "__main__":
    main()