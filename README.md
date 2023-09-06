VAT Rates
=========
![build status](https://github.com/github/docs/actions/workflows/python-app.yml/badge.svg)

This repository is a maintained fork from [adamcooke/vat-rates](https://github.com/adamcooke/vat-rates) and hosts a community maintained collection of EU VAT rates.

Its primary purpose is to provide an up-to-date resource of VAT rates for EU member states.

Pull requests for updated VAT rates are closely monitored and more than welcome.

## Usage

You can fetch the JSON resource from GitHub directly. We recommend storing a local copy and refreshing it periodically (or use a client library that handles this for you).

```sh
curl https://raw.githubusercontent.com/ibericode/vat-rates/master/vat-rates.json
```

## Client libraries

The following client libraries are available right now.

**PHP**:

- [ibericode/vat](https://github.com/ibericode/vat)

**Golang**

- [dannyvankooten/vat](https://github.com/dannyvankooten/vat)

## Disclaimer

This repository is provided on an as-is basis. The authors or contributors cannot be held responsible for its accuracy or completeness. 

## License

MIT licensed. See [LICENSE](LICENSE) for details.